import unittest
import snake

class TestYourScore(unittest.TestCase):
  def setUp(self):
    pygame.init()

  def test_your_score(self):
    # Initialize screen for testing
    screen = pygame.Surface((800, 600))

    # Call the function
    Your_score(1)

    # Check if the score is rendered correctly
    rendered_text = screen.get_at((0, 0))
    self.assertEqual(rendered_text, pygame.Color('yellow'))

  def tearDown(self):
    pygame.quit()

if __name__ == '__main__':
    unittest.main()
