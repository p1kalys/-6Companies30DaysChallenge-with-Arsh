class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int cloestX = max(x1, min(xCenter, x2));
        int cloesty = max(y1, min(yCenter, y2));

        int distX = xCenter -cloestX;
        int distY = yCenter -cloesty;

        int sqDist = distX*distX + distY*distY;
        return sqDist <= radius*radius;
    }
};
