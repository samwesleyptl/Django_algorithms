from django.test import TestCase
from ac_data.algorithms import optimize_energy

class OptimizeEnergyTest(TestCase):
    
    def test_increase_ac_temp_due_to_high_room_temp_and_humidity(self):
        """Test that AC temp increases when room temp is above 25 and humidity is above 60"""
        room_temp = 27
        ac_temp = 22
        humidity = 65
        new_ac_temp, energy_saving_factor = optimize_energy(room_temp, ac_temp, humidity)
        
        self.assertEqual(new_ac_temp, ac_temp + 1)
        self.assertTrue(0 <= energy_saving_factor <= 1)
    
    def test_decrease_ac_temp_due_to_low_room_temp(self):
        """Test that AC temp decreases when room temp is below 20"""
        room_temp = 18
        ac_temp = 22
        humidity = 50
        new_ac_temp, energy_saving_factor = optimize_energy(room_temp, ac_temp, humidity)
        
        self.assertEqual(new_ac_temp, ac_temp - 1)
        self.assertTrue(0 <= energy_saving_factor <= 1)
    
    def test_no_change_in_ac_temp(self):
        """Test that AC temp stays the same when conditions do not warrant a change"""
        room_temp = 22
        ac_temp = 24
        humidity = 50
        new_ac_temp, energy_saving_factor = optimize_energy(room_temp, ac_temp, humidity)
        
        self.assertEqual(new_ac_temp, ac_temp)
        self.assertTrue(0 <= energy_saving_factor <= 1)

    def test_energy_saving_factor_bounds(self):
        """Test that energy saving factor is between 0 and 1"""
        room_temp = 26
        ac_temp = 22
        humidity = 65
        new_ac_temp, energy_saving_factor = optimize_energy(room_temp, ac_temp, humidity)

        # Energy-saving factor should be between 0 and 1
        self.assertGreaterEqual(energy_saving_factor, 0)
        self.assertLessEqual(energy_saving_factor, 1)
