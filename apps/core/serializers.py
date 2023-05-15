from rest_framework import serializers
from apps.core.utils import get_priority


class FigthSerializer(serializers.Serializer):
    movimientos = serializers.ListField(
        child=serializers.CharField(max_length=5, allow_blank=True)
    )
    golpes = serializers.ListField(
        child=serializers.CharField(max_length=1, allow_blank=True)
    )


class CombatSerializer(serializers.Serializer):
    player1 = FigthSerializer()
    player2 = FigthSerializer()

    def move(self, player: int):
        match player:
            case 1:
                se_movio_a_la_derecha = self.player_1_movements.count("D")
                if se_movio_a_la_derecha and self.espacios_entre_si == 1:
                    self.espacios_entre_si -= 1
                se_movio_a_la_izquierda = self.player_1_movements.count("A")
                if se_movio_a_la_izquierda and self.espacios_entre_si == 0:
                    self.espacios_entre_si += 1
            case 2:
                se_movio_a_la_derecha = self.player_2_movements.count("D")
                if se_movio_a_la_derecha and self.espacios_entre_si == 0:
                    self.espacios_entre_si += 1
                se_movio_a_la_izquierda = self.player_2_movements.count("A")
                if se_movio_a_la_izquierda and self.espacios_entre_si == 1:
                    self.espacios_entre_si -= 1

    def evade(self, player: int):
        evade_relation = {"K": "S", "P": "W"}
        match player:
            case 1:
                if self.damage_player_2 not in [0, 1] and self.player_2_golpes:
                    self.evade_1 = self.player_1_movements.count(
                        evade_relation[self.player_2_golpes]
                    )
            case 2:
                if self.damage_player_1 in [0, 1] and self.player_1_golpes:
                    self.evade_2 = self.player_2_movements.count(
                        evade_relation[self.player_1_golpes]
                    )

    def apply_damage(self):
        if self.priority == 1:
            self.move(1)
            if self.espacios_entre_si == 0:
                if self.name_atack_1:
                    self.history.append(f"Tony da un {self.name_atack_1}")
                self.energy_2 = self.energy_2 - self.damage_player_1
            self.move(2)
            if self.espacios_entre_si == 0:
                if self.name_atack_1:
                    self.history.append(f"Arnaldor da un {self.name_atack_2}")
                self.energy_1 = self.energy_1 - self.damage_player_2
            if self.energy_2 <= 0:
                self.champion = 1
                return
            if self.energy_1 <= 0:
                self.champion = 2
                return
        # Ataca primero el jugador 2
        else:
            self.move(1)
            if self.espacios_entre_si == 0:
                self.energy_1 = self.energy_1 - self.damage_player_2

            self.move(2)
            if self.espacios_entre_si == 0:
                self.energy_2 = self.energy_2 - self.damage_player_1
            if self.energy_1 <= 0:
                self.champion = 2
                return
            if self.energy_2 <= 0:
                self.champion = 1
                return

    def create(self, data):
        self.history = []
        self.champion = None
        # Seteamos los rounds
        movements_limit_1 = len(data["player1"]["movimientos"])
        movements_limit_2 = len(data["player2"]["movimientos"])
        # Seteamos data para saber si se pueden dar o no
        vector_data = {"cerca": False, "jugador": None, "vector": 0}
        # Presentamos los combos del jugador 1
        self.combo_player_1 = {
            "DSD + P": {"damage": 3, "name": "Taladoken"},
            "SD + K": {"damage": 2, "name": "Remuyuken"},
        }
        # Presentamos los combos del jugador 2
        self.combo_player_2 = {
            "SA + K": {"damage": 3, "name": "Remuyuken"},
            "ASA + P": {"damage": 2, "name": "Taladoken"},
        }
        self.espacios_entre_si = 1
        self.energy_1, self.energy_2 = 6, 6
        for i in range(
            0,
            movements_limit_1
            if movements_limit_1 >= movements_limit_2
            else movements_limit_2,
        ):
            self.damage_player_1 = 1
            try:
                self.player_1_movements = data["player1"]["movimientos"][i]
            except IndexError:
                self.player_1_movements = ""
            try:
                self.player_1_golpes = data["player1"]["golpes"][i]
            except IndexError:
                self.player_1_golpes = ""

            self.combo_player_1_realizar = (
                f"{self.player_1_movements} + {self.player_1_golpes}"
            )
            if self.combo_player_1_realizar in ["DSD + P", "SD + K"]:
                self.name_atack_1 = self.combo_player_1[self.combo_player_1_realizar][
                    "name"
                ]
                self.damage_player_1 = self.combo_player_1[
                    self.combo_player_1_realizar
                ]["damage"]
            else:
                if self.player_1_golpes:
                    self.name_atack_1 = (
                        "Patada" if self.player_1_golpes == "K" else "Puño"
                    )
            # Verificamos si hay un combo especial sino solo se queda con el daño =1 (Player2)
            self.damage_player_2 = 1
            try:
                self.player_2_movements = data["player2"]["movimientos"][i]
            except IndexError:
                self.player_2_movements = ""
            try:
                self.player_2_golpes = data["player2"]["golpes"][i]
            except IndexError:
                self.player_2_golpes = ""
            self.combo_player_2_realizar = (
                f"{self.player_2_movements} + {self.player_2_golpes}"
            )
            if self.combo_player_2_realizar in ["SA + K", "ASA + P"]:
                self.name_atack_2 = self.combo_player_2[self.combo_player_2_realizar][
                    "name"
                ]
                self.damage_player_2 = self.combo_player_2[
                    self.combo_player_2_realizar
                ]["damage"]
            else:
                if self.player_2_golpes:
                    self.name_atack_2 = (
                        "Patada" if self.player_2_golpes == "K" else "Puño"
                    )
            self.priority = get_priority(
                {
                    "combo_player_1": self.combo_player_1_realizar,
                    "movements_player_1": self.player_1_movements,
                    "golpes_player_1": self.player_1_golpes,
                    "combo_player_2": self.combo_player_2_realizar,
                    "movements_player_2": self.player_2_movements,
                    "golpes_player_2": self.player_2_golpes,
                }
            )
            self.apply_damage()
            if self.champion:
                self.history.append(
                    f"Gana el jugador {self.champion} quedando con {max(self.energy_1, self.energy_2)} de energia"
                )
                break
        return self.energy_1, self.energy_2, self.champion, self.history
