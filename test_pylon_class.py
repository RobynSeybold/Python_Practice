import unittest
import pylon_class

class TestPylon(unittest.TestCase):
    
    def test_protosswarp(self):
        
        #Test if probes are correctly ignored.
        front = {"Probe":1}
        base = {"Probe":2}
        
        pylon = pylon_class.Pylon(front)
        output_base, output_front = pylon.protoss_warp(base)

        self.assertEqual(output_base, base)
        self.assertEqual(output_front, front)

        #Test if units are correctly stacked.
        front = {"Zealot":3}
        base = {"Zealot":5}
        
        pylon = pylon_class.Pylon(front)
        output_base, output_front = pylon.protoss_warp(base)

        self.assertEqual(output_base["Zealot"], 0)
        self.assertEqual(output_front["Zealot"], 8)

        #Test to avoid repeat error with empty dictionaries.
        front = {}
        base = {"Zealot":2}
        
        pylon = pylon_class.Pylon(front)
        output_base, output_front = pylon.protoss_warp(base)

        self.assertEqual(output_base["Zealot"], 0)
        self.assertEqual(output_front["Zealot"], 2)

        #Test to see if units are correctly added to the new dictionary.
        front = {"Zealot":1}
        base = {"Archon":1}
        
        pylon = pylon_class.Pylon(front)
        output_base, output_front = pylon.protoss_warp(base)

        self.assertEqual(output_base["Archon"], 0)
        self.assertEqual(output_front["Archon"], 1)
       
        
unittest.main()



