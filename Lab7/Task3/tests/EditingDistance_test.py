import unittest
from random import randint

from Lab7.Task3.src.EditingDistance import main, editing_distance, editing_distance_memory_optimized
from utils import time_data, memory_data


class TestEditingDistance(unittest.TestCase):
    def test_editing_distance_no_actions(self):
        # given
        data = [('word1', 'word2'), ('editing', 'distance'),
                ('ports', 'short'), ('abc', 'abc'), ('a', '')]
        expected_results = [1, 5, 3, 0, 1]

        for index, words in enumerate(data):
            # when
            result = editing_distance_memory_optimized(words[0], words[1])

            # then
            self.assertEqual(result, expected_results[index])

    def test_editing_distance_with_actions_random(self):
        # given
        word_will_change = "".join([chr(randint(ord('a'), ord('z'))) for _ in range(randint(5, 10))])
        word = "".join([chr(randint(ord('a'), ord('z'))) for _ in range(randint(5, 10))])
        result_container = [[] if i % 2 == 0 else word_will_change[i // 2] for i in range(len(word_will_change) * 2)]

        # when
        cnt = 0
        for action in editing_distance(word_will_change, word):
            cnt += 1
            command, *values = action.split()
            if command == 'del':
                result_container[int(values[2]) * 2 + 1] = None
            elif command == 'add':
                result_container[int(values[2]) * 2].append(values[0])
            elif command == 'change':
                result_container[int(values[3]) * 2 + 1] = values[1]

        result = []
        for i in range(len(result_container)):
            if i % 2 == 0:
                for element in result_container[i]:
                    result.append(element)
            else:
                if result_container[i] is not None:
                    result.append(result_container[i])

        # then
        self.assertEqual("".join(result), word)
        self.assertEqual(cnt, editing_distance_memory_optimized(word_will_change, word))

    def test_time(self):
        # when
        time = time_data(main)
        # then
        self.assertLess(time, 1)

    def test_memory_data(self):
        # when
        cur, peak = memory_data(main)
        # then
        self.assertLess(cur, 2)
        self.assertLess(peak, 2)


if __name__ == "__main__":
    unittest.main()
