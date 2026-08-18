from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse

from .models import Park, Trail


class TrailTests(TestCase):

    def setUp(self):
        self.park = Park.objects.create(
            name="Test Park",
            region="Test Region",
        )

        self.open_trail = Trail.objects.create(
            name="Open Trail",
            park=self.park,
            distance_km=Decimal("10.00"),
            elevation_gain=100,
            difficulty="easy",
            is_open=True,
        )

        self.closed_trail = Trail.objects.create(
            name="Closed Trail",
            park=self.park,
            distance_km=Decimal("5.00"),
            elevation_gain=50,
            difficulty="moderate",
            is_open=False,
        )

    def test_open_trails_query(self):
        trails = Trail.objects.filter(
            is_open=True
        ).order_by("distance_km")

        self.assertEqual(list(trails), [self.open_trail])
        self.assertNotIn(self.closed_trail, trails)

    def test_trail_detail_404(self):
        response = self.client.get(
            reverse("trail_detail", args=[9999])
        )

        self.assertEqual(response.status_code, 404)

    def test_invalid_difficulty_rejected(self):
        trail = Trail(
            name="Invalid Trail",
            park=self.park,
            distance_km=Decimal("5.00"),
            elevation_gain=100,
            difficulty="impossible",
            is_open=True,
        )

        with self.assertRaises(ValidationError):
            trail.full_clean()