import unittest
from app.models import Comment

class CommentModelTest(unittest.TestCase):

    def setUp(self):
        self.new_comment = Comment(comment = 'I like my life', user_id=1)

    # def test_instance(self):
    #     self.assertTrue(isinstance(self.new_comment, Comment))

    # def test_save_comment(self):
    #     self.new_comment.save_comment()
    #     self.assertTrue(len(Comment.query.all())>0)  