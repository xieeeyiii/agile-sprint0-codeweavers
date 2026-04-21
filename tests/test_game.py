import unittest
import sys
sys.path.insert(0, ".")

from map import MazeMap
from player import Player
from command import CommandHandler
import constants as c

class TestMazeGameTDD(unittest.TestCase):
    def setUp(self):
        self.maze = MazeMap()
        self.player = Player()
        self.cmd = CommandHandler(self.maze, self.player)

    # 测试 1：撞墙不会移动
    def test_player_cannot_move_into_wall(self):
        # 玩家初始位置 (1,1)，往上是墙，移动无效
        self.cmd.handle_move("w")
        self.assertEqual(self.maze.player_y, 1)  # 位置不变

    # 测试 2：玩家可以正常拾取物品 K
    def test_player_pick_item(self):
        self.cmd.handle_move("d")  # 向右走到物品位置
        self.assertEqual(self.player.inventory, ["K"])

    # 测试 3：无效命令不会让游戏崩溃
    def test_invalid_command(self):
        self.cmd.process_input("abc123")
        self.assertTrue(self.cmd.game_running)

if __name__ == '__main__':
    unittest.main()
