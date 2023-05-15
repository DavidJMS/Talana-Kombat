def get_priority(movements: dict):
    # Nos guiamos del combo
    if len(movements["combo_player_1"]) < len(movements["combo_player_2"]):
        # print("Combo", movements["combo_player_1"], movements["combo_player_2"])
        return 1
    elif len(movements["combo_player_1"]) > len(movements["combo_player_2"]):
        # print("Combo", movements["combo_player_1"], movements["combo_player_2"])
        return 2
    # Nos guiamos de los movimientos
    if len(movements["movements_player_1"]) < len(movements["movements_player_2"]):
        # print(
        #     "Movimiento",
        #     movements["movements_player_1"],
        #     movements["movements_player_2"],
        # )
        return 1
    elif len(movements["movements_player_1"]) > len(movements["movements_player_2"]):
        # print(
        #     "Movimiento",
        #     movements["movements_player_1"],
        #     movements["movements_player_2"],
        # )
        return 2
    # Nos guiamos de los golpes
    if len(movements["golpes_player_1"]) < len(movements["golpes_player_2"]):
        # print("Golpes", movements["golpes_player_1"], movements["golpes_player_2"])
        return 1
    elif len(movements["golpes_player_1"]) > len(movements["golpes_player_2"]):
        # print("Golpes", movements["golpes_player_1"], movements["golpes_player_2"])
        return 2
    # Vale madres el 1 es el mejor jeje
    return 1
