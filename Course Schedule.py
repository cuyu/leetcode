"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
"""
from __future__ import annotations

from typing import List, Tuple


class Course(object):
    def __init__(self, name):
        self._name = name
        self._prerequisites = set()

    def update(self, prerequisite: List[Course]):
        if prerequisite[0] == self:
            self._prerequisites.add(prerequisite[1])

    @property
    def prerequisites(self):
        return self._prerequisites

    def can_finish(self, courses: Tuple[Course]) -> bool:
        dependent_courses = (self, *courses)
        for c in dependent_courses:
            if c in self.prerequisites:
                return False
        for course in self._prerequisites:
            if not course.can_finish(dependent_courses):
                return False
        return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        all_courses = []
        for i in range(numCourses):
            course = Course(i)
            all_courses.append(course)
        for course in all_courses:
            for pair in prerequisites:
                course.update([all_courses[pair[0]], all_courses[pair[1]]])
        for course in all_courses:
            if not course.can_finish(tuple()):
                return False
        return True


if __name__ == '__main__':
    # print(Solution().canFinish(4, [[0, 1], [2, 3], [1, 2], [3, 0]]))
    print(Solution().canFinish(3, [[0, 1], [0, 2], [1, 2]]))
