import unittest
import sys
sys.path.insert(0, ".")

from map import MazeMap
from player import Player
from command import CommandHandler
import constants as c

class TestMazeGameTDD(unittest.TestCase):
    def setUp(self):
        # 初始化游戏
        self.maze = MazeMap()
        self.player = Player()
        self.cmd = CommandHandler(self.maze, self.player)

    # 测试 1：玩家不能走出地图边界
    def test_player_cannot_move_out_of_border(self):
        # 玩家初始位置 (1,1)
        self.cmd.handle_move("w")
        self.cmd.handle_move("w")
        self.assertEqual(self.maze.player_y, 0)  # 不会再动

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
