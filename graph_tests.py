import unittest
from graph import *


class TestList(unittest.TestCase):

    def test_01(self):
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertTrue(g.is_bipartite())
        self.assertEqual(g.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

    def test_02(self):
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])
        self.assertFalse(g.is_bipartite())

    def test_init(self):
        g1 = Graph('test1.txt')
        self.assertEqual(g1.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        g2 = Graph('test2.txt')
        self.assertEqual(g2.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v6', 'v7', 'v8'])

    def test_add_vertex(self):
        g1 = Graph('test1.txt')
        self.assertEqual(g1.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        # not already in
        g1.add_vertex('v0')
        self.assertEqual(g1.get_vertices(), ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        # already in
        g1.add_vertex('v4')
        self.assertEqual(g1.get_vertices(), ['v0', 'v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])

    def test_get_vertex(self):
        g1 = Graph('test1.txt')
        self.assertEqual(g1.get_vertex('this vertex does not exist'), None)

    def test_add_edge(self):
        g1 = Graph('test1.txt')
        self.assertEqual(g1.get_vertices(), ['v1', 'v2', 'v3', 'v4', 'v5', 'v6', 'v7', 'v8', 'v9'])
        # v1
        self.assertEqual(g1.adj_list[0].adjacent_to, ['v2', 'v3', 'v4', 'v5'])
        # v2
        self.assertEqual(g1.adj_list[1].adjacent_to, ['v1'])
        # v6
        self.assertEqual(g1.adj_list[5].adjacent_to, ['v7', 'v8'])

    def test_conn_components(self):
        # test for two given files
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        g = Graph('test2.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3'], ['v4', 'v6', 'v7', 'v8']])

        # ensure that conn_components will be able to be called multiple times (issue encountered earlier)
        g = Graph('test1.txt')
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])
        self.assertEqual(g.conn_components(), [['v1', 'v2', 'v3', 'v4', 'v5'], ['v6', 'v7', 'v8', 'v9']])

    def test_is_bipartite(self):
        g = Graph('test1.txt')
        self.assertTrue(g.is_bipartite())
        g = Graph('test2.txt')
        self.assertFalse(g.is_bipartite())
        g = Graph('test3.txt')
        self.assertTrue(g.is_bipartite())

        # ensure that is_bipartite will be able to be called multiple times (issue encountered earlier)
        g = Graph('test1.txt')
        self.assertTrue(g.is_bipartite())
        self.assertTrue(g.is_bipartite())
        self.assertTrue(g.is_bipartite())
        self.assertTrue(g.is_bipartite())
        self.assertTrue(g.is_bipartite())
        g = Graph('test4.txt')
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())
        self.assertFalse(g.is_bipartite())


if __name__ == '__main__':
    unittest.main()
