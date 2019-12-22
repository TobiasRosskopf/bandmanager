import unittest
from django.test import TestCase

# Import models
from .models import Song
from .models import Gig


# Tests for Song model
class SongTestCase(TestCase):
    def setUp(self):
        Song.objects.create(name="ABC", interpret="Jackson 5")
        Song.objects.create(name="Song 2", interpret="Blur")

    def test_song_str(self):
        song1 = Song.objects.get(name="ABC")
        song2 = Song.objects.get(name="Song 2")
        self.assertEqual(str(song1), "ABC (Jackson 5)")
        self.assertEqual(str(song2), "Song 2 (Blur)")

    def test_duration_mmss(self):
        song1 = Song.objects.get(name="ABC")
        self.assertEqual(song1.duration_mmss(), "00:00")


# Tests for Gig model
class GigTestCase(TestCase):
    def setUp(self):
        Gig.objects.create(date="2019-06-07", location="Rock am Ring")
        Gig.objects.create(date="2020-12-31", location="Timesquare New York")

    def test_gig_str(self):
        gig1 = Gig.objects.get(date="2019-06-07")
        gig2 = Gig.objects.get(date="2020-12-31")
        self.assertEqual(str(gig1), "07.06.2019 - Rock am Ring")
        self.assertEqual(str(gig2), "31.12.2020 - Timesquare New York")

    def test_time_hhmm(self):
        gig1 = Gig.objects.get(date="2019-06-07")
        self.assertEqual(gig1.time_hhmm(), "00:00")
