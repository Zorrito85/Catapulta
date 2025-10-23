import unittest
from catapulta.catapult import Catapult
from catapulta.parts.stick import Stick
from catapulta.parts.rubber_band import RubberBand
from catapulta.parts.glue import Glue
from catapulta.parts.bottle_cap import BottleCap
from catapulta.parts.paper_clip import PaperClip

class TestCatapult(unittest.TestCase):

    def setUp(self):
        self.catapult = Catapult()
        self.stick = Stick()
        self.rubber_band = RubberBand()
        self.glue = Glue()
        self.bottle_cap = BottleCap()
        self.paper_clip = PaperClip()

    def test_add_part(self):
        self.catapult.add_part(self.stick)
        self.catapult.add_part(self.rubber_band)
        self.catapult.add_part(self.glue)
        self.catapult.add_part(self.bottle_cap)
        self.catapult.add_part(self.paper_clip)

        self.assertIn(self.stick, self.catapult.parts)
        self.assertIn(self.rubber_band, self.catapult.parts)
        self.assertIn(self.glue, self.catapult.parts)
        self.assertIn(self.bottle_cap, self.catapult.parts)
        self.assertIn(self.paper_clip, self.catapult.parts)

    def test_launch_projectile(self):
        self.catapult.add_part(self.stick)
        self.catapult.add_part(self.rubber_band)
        projectile = self.catapult.launch_projectile()

        self.assertIsNotNone(projectile)
        self.assertEqual(projectile.weight, 1)  # Assuming default weight
        self.assertGreater(projectile.velocity, 0)  # Assuming it should have some velocity

if __name__ == '__main__':
    unittest.main()