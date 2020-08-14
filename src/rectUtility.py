def isSubinterval(aStart, aEnd, bStart, bEnd, tolerance=0):
    return aStart + tolerance >= bStart and aEnd - tolerance <= bEnd


def intersects(aStart, aEnd, bStart, bEnd):
    return not (aEnd < bStart or aStart > bEnd)


class Rectangle:
    def __init__(self, l, t, r, b):
        self.left = l
        self.top = t
        self.right = r
        self.bottom = b
        self.enclosedByHowManyRectangles = 0
        self.sameWithHowManyRectangles = 0

    def isSameRectangle(self, other, tolerance=0):
        if self.left-(other.left) in range(-1*tolerance,tolerance+1)\
            and self.top-(other.top) in range(-1*tolerance,tolerance+1)\
            and self.right-(other.right) in range(-1*tolerance,tolerance+1)\
            and self.bottom-(other.bottom) in range(-1*tolerance,tolerance+1):
            self.sameWithHowManyRectangles = self.sameWithHowManyRectangles + 1
            return True
        return False

    def isSubrectangle(self, other, tolerance=0):
        if (isSubinterval(self.left, self.right, other.left, other.right,
                          tolerance)
                and isSubinterval(self.top, self.bottom, other.top,
                                  other.bottom, tolerance)):
            self.enclosedByHowManyRectangles = self.enclosedByHowManyRectangles + 1
            return True

    def intersects(self, other):
        return (intersects(self.left, self.right, other.left, other.right)
                and intersects(self.top, self.bottom, other.top, other.bottom))

    def __repr__(self):
        return ("[%f,%f]x[%f,%f]" %
                (self.left, self.top, self.right, self.bottom))


def boundingBox(rects):
    infty = float('inf')
    b = infty
    t = -infty
    l = infty
    r = -infty
    for rect in rects:
        b = min(b, rect.bottom)
        l = min(l, rect.left)
        r = max(r, rect.right)
        t = max(t, rect.top)
    return Rectangle(l, r, b, t)


class DividingLine:
    def __init__(self, isHorizontal, position):
        self.isHorizontal = isHorizontal
        self.position = position

    def isAbove(self, rectangle):
        if self.isHorizontal:
            return rectangle.bottom > self.position
        else:
            return rectangle.left > self.position

    def isBelow(self, rectangle):
        if self.isHorizontal:
            return rectangle.top < self.position
        else:
            return rectangle.right < self.position


def enumeratePossibleLines(boundingBox):
    NUM_TRIED_LINES = 5
    for i in range(1, NUM_TRIED_LINES + 1):
        w = boundingBox.right - boundingBox.left
        yield DividingLine(
            False, boundingBox.left + w / float(NUM_TRIED_LINES + 1) * i)
        h = boundingBox.top - boundingBox.bottom
        yield DividingLine(
            True, boundingBox.bottom + h / float(NUM_TRIED_LINES + 1) * i)


def findGoodDividingLine(rects_1, rects_2):
    bb = boundingBox(rects_1 + rects_2)
    bestLine = None
    bestGain = 0
    for line in enumeratePossibleLines(bb):
        above_1 = len([r for r in rects_1 if line.isAbove(r)])
        below_1 = len([r for r in rects_1 if line.isBelow(r)])
        above_2 = len([r for r in rects_2 if line.isAbove(r)])
        below_2 = len([r for r in rects_2 if line.isBelow(r)])

        # These groups are separated by the line, no need to
        # perform all-vs-all collision checks on those groups!
        gain = above_1 * below_2 + above_2 * below_1
        if gain > bestGain:
            bestGain = gain
            bestLine = line
    return bestLine


# Collides all rectangles from list `rects_1` with
# all rectangles from list `rects_2`, and invokes
# `onCollision(a, b)` on every colliding `a` and `b`.
def collideAllVsAll(rects_1, rects_2, onCollision):
    if rects_1 and rects_2:  # if one list empty, no collisions
        line = findGoodDividingLine(rects_1, rects_2)
        if line:
            above_1 = [r for r in rects_1 if line.isAbove(r)]
            below_1 = [r for r in rects_1 if line.isBelow(r)]
            above_2 = [r for r in rects_2 if line.isAbove(r)]
            below_2 = [r for r in rects_2 if line.isBelow(r)]
            intersect_1 = [
                r for r in rects_1 if not (line.isAbove(r) or line.isBelow(r))
            ]
            intersect_2 = [
                r for r in rects_2 if not (line.isAbove(r) or line.isBelow(r))
            ]

            if (above_1 == rects_1 and above_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(above_1, above_2, onCollision)

            if (above_1 == rects_1 and intersect_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(above_1, intersect_2, onCollision)

            if (intersect_1 == rects_1 and above_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(intersect_1, above_2, onCollision)

            if (intersect_1 == rects_1 and intersect_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(intersect_1, intersect_2, onCollision)

            if (intersect_1 == rects_1 and below_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(intersect_1, below_2, onCollision)

            if (below_1 == rects_1 and intersect_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(below_1, intersect_2, onCollision)

            if (below_1 == rects_1 and below_2 == rects_2):
                for r1 in rects_1:
                    for r2 in rects_2:
                        if r1.intersects(r2):
                            onCollision(r1, r2)
            else:
                collideAllVsAll(below_1, below_2, onCollision)
        else:
            for r1 in rects_1:
                for r2 in rects_2:
                    if r1.intersects(r2):
                        onCollision(r1, r2)
