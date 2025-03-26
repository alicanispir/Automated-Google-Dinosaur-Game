import pyautogui
import time
from PIL import ImageGrab, ImageOps, Image
import pygetwindow as gw

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
DINO_IMAGE_PATH = "dino.png"
CACTUS_IMAGE_PATH = "interaction_cactus_dino.png"
DETECTION_DELAY = 0.05

def focus_game_window():
    """Ensure the game window is active."""
    try:
        game_window = gw.getWindowsWithTitle('Dinosaur Game')[0]
        if game_window:
            game_window.minimize()
            time.sleep(0.1)
            game_window.restore()
            time.sleep(0.1)
            print("Game window focused.")
            return True
    except IndexError:
        print("Game window not found.")
        return False
def detect_cactus():
    """Detect cactus using image recognition."""
    screen = ImageGrab.grab(bbox=(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.save("test_screenshot.png")
    print("Screenshot saved! Check 'test_screenshot.png'.")
    screen_gray = ImageOps.grayscale(screen)

    try:
        cactus_location = pyautogui.locate(Image.open(CACTUS_IMAGE_PATH).convert("L"), screen_gray, confidence=0.5)
        if cactus_location:
            print("Cactus detected at:", cactus_location)
            return True
    except:
        print("interaction with cactus was not found!")
        return False

def make_dino_jump():
    """Make the dino jump by pressing the UP key."""
    pyautogui.press('up')
    print("Jump command sent!")

def game_loop():
    """Main game loop to detect cacti and make the dino jump."""
    if not focus_game_window():
        return
    while True:
        game_window = gw.getWindowsWithTitle('Dinosaur Game')
        if not game_window:
            print("Game window closed. Exiting game loop.")
            break
        if detect_cactus():
            make_dino_jump()
        time.sleep(DETECTION_DELAY)

if __name__ == "__main__":
    game_loop()