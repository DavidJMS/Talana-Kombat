import pytest
from django.urls import reverse
from rest_framework.test import APIClient


@pytest.mark.django_db
@pytest.mark.parametrize(
    "player1, player2, winner",
    [
        (
            {
                "movimientos": ["D", "DSD", "S", "DSD", "SD"],
                "golpes": ["K", "P", "", "K", "P"],
            },
            {
                "movimientos": ["SA", "SA", "SA", "ASA", "SA"],
                "golpes": ["K", "", "K", "P", "P"],
            },
            2,
        ),
        (
            {
                "movimientos": ["SDD", "DSD", "SA", "DSD"],
                "golpes": ["K", "P", "K", "P"],
            },
            {
                "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
                "golpes": ["P", "K", "K", "K", "P", "k"],
            },
            1,
        ),
        (
            {"movimientos": ["DSD", "S"], "golpes": ["P", ""]},
            {
                "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
                "golpes": ["P", "", "P", "K", "K", "K"],
            },
            2,
        ),
    ],
)
def test_view(player1, player2, winner):
    url = reverse("core:fight")
    data = {"player1": player1, "player2": player2}
    response = APIClient().post(url, data=data, format="json")
    assert winner == response.data["data"]["ganador"]
