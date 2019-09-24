
import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(pitch = 'Life is good.', category_id = 1, user_id=1)


    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_pitch, Pitch))

    # def test_save_comment(self):
    #     self.new_pitch.save_pitch()
    #     self.assertTrue(len(Pitch.query.all())>0)