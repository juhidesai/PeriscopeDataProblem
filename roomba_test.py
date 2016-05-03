import unittest
from roomba import *
class TestRoomba(unittest.TestCase):

    def test1(self):
        f = open("input.txt","w")
        f.write("""5 5
1 2
1 0
2 2
2 3
NNESEESWNWW
                """)
        f.close()
        dirt_patches, instructions, roomx, roomy, hooverx, hoovery = read_file()
        dirt_count = 0
        for instruction in instructions:        
            hooverx, hoovery, dirt_count = traverse(dirt_patches, instruction, roomx, roomy, hooverx, hoovery, dirt_count)
        self.assertEqual(hooverx,1)
        self.assertEqual(hoovery,3)
        self.assertEqual(dirt_count,1)
        
    def test2(self):
        f = open("input.txt","w")
        f.write("""5 5
1 2
1 0
2 2
2 3
2 4
NNESEESWNWW
                """)
        f.close()
        dirt_patches, instructions, roomx, roomy, hooverx, hoovery = read_file()
        dirt_count = 0
        for instruction in instructions:        
            hooverx, hoovery, dirt_count = traverse(dirt_patches, instruction, roomx, roomy, hooverx, hoovery, dirt_count)
        self.assertEqual(hooverx,1)
        self.assertEqual(hoovery,3)
        self.assertEqual(dirt_count,2)

    def test3(self):
        f = open("input.txt","w")
        f.write("""5 5
1 2
NNESEESWNWW
                """)
        f.close()
        dirt_patches, instructions, roomx, roomy, hooverx, hoovery = read_file()
        dirt_count = 0
        for instruction in instructions:        
            hooverx, hoovery, dirt_count = traverse(dirt_patches, instruction, roomx, roomy, hooverx, hoovery, dirt_count)
        self.assertEqual(hooverx,1)
        self.assertEqual(hoovery,3)
        self.assertEqual(dirt_count,0)

    def test4(self):
        f = open("input.txt","w")
        f.write("""5 5
0 0
1 1
2 1
3 2
4 1
NNESEESWNWW
                """)
        f.close()
        dirt_patches, instructions, roomx, roomy, hooverx, hoovery = read_file()
        dirt_count = 0
        for instruction in instructions:        
            hooverx, hoovery, dirt_count = traverse(dirt_patches, instruction, roomx, roomy, hooverx, hoovery, dirt_count)
        self.assertEqual(hooverx,0)
        self.assertEqual(hoovery,1)
        self.assertEqual(dirt_count,2)

    def test_read_file(self):
        dirt_patches, instructions, roomx, roomy, hooverx, hoovery = read_file()
        self.assertIsNotNone(dirt_patches)
        self.assertEqual(instructions,"NNESEESWNWW")
        self.assertEqual(roomx,5)
        self.assertEqual(roomy,5)
        self.assertEqual(hooverx,0)
        self.assertEqual(hoovery,0)

    def test_traverse(self):
        dirt_patches = {}
        dirt_patches[3]=[1,3]
        hooverx, hoovery, dirt_count = traverse(dirt_patches, "N", 5, 5, 3, 2, 0)
        self.assertEqual(hooverx,3)
        self.assertEqual(hoovery,3)
        self.assertEqual(dirt_count,1)

    def test_clean_dirt(self):
        dirt_patches = {}
        dirt_patches[3]=[3]
        dirt_count = clean_dirt(3, 3, 1, dirt_patches)
        self.assertEqual(dirt_count,2)

if __name__ == "__main__":
    unittest.main()
