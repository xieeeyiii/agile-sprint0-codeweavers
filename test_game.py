# 迭代4 AI辅助测试 - 单元测试
import sys
sys.path.append("./backend")

import pytest
from app import app
from player import Player

# 测试1：拾取物品
def test_pick_item():
    p = Player()
    p.pick_item("key")
    assert "key" in p.inventory

# 测试2：重复拾取不重复添加
def test_pick_duplicate():
    p = Player()
    p.pick_item("key")
    p.pick_item("key")
    assert len(p.inventory) == 1

# 测试3：未生成迷宫移动 → 报错
def test_move_before_generate():
    client = app.test_client()
    res = client.get("/api/move-player/w")
    assert res.status_code == 400

# 测试4：生成迷宫 + 正常移动
def test_generate_and_move():
    client = app.test_client()
    client.get("/api/generate-maze")
    res = client.get("/api/move-player/d")
    data = res.get_json()
    assert data["success"] is True