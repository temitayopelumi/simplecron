import unittest
from cron_praser import parse_field, parse_cron, format_output

class TestCronParser(unittest.TestCase):

    def test_parse_field_star(self):
        result = parse_field('*', 0, 59)
        self.assertEqual(result, list(range(0, 60)))

    def test_parse_field_range(self):
        result = parse_field('1-5', 0, 59)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_parse_field_step(self):
        result = parse_field('*/15', 0, 59)
        self.assertEqual(result, [0, 15, 30, 45])

    def test_parse_field_multiple(self):
        result = parse_field('1,3,5', 0, 59)
        self.assertEqual(result, [1, 3, 5])

    def test_parse_field_range_step(self):
        result = parse_field('10-20/5', 0, 59)
        self.assertEqual(result, [10, 15, 20])

    def test_parse_field_invalid(self):
        with self.assertRaises(ValueError):
            parse_field('100', 0, 59)
        with self.assertRaises(ValueError):
            parse_field('5-1', 0, 59)
        with self.assertRaises(ValueError):
            parse_field('*/0', 0, 59)
        with self.assertRaises(ValueError):
            parse_field('', 0, 59)

    def test_parse_cron_valid(self):
        cron_line = '0 12 * * * /usr/bin/somecommand'
        parsed = parse_cron(cron_line)
        expected = {
            'minute': [0],
            'hour': [12],
            'day_of_month': list(range(1, 32)),
            'month': list(range(1, 13)),
            'day_of_week': list(range(0, 7)),
            'command': '/usr/bin/somecommand'
        }
        self.assertEqual(parsed, expected)

    def test_parse_cron_invalid(self):
        with self.assertRaises(ValueError):
            parse_cron('invalid cron line')

    def test_format_output(self):
        cron_line = '0 12 * * * /usr/bin/somecommand'
        parsed = parse_cron(cron_line)
        output = format_output(parsed)
        self.assertIn("minute", output)
        self.assertIn("hour", output)
        self.assertIn("day_of_month", output)
        self.assertIn("month", output)
        self.assertIn("day_of_week", output)
        self.assertIn("/usr/bin/somecommand", output)

if __name__ == '__main__':
    unittest.main()