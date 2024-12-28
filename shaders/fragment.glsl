#version 330 core

in vec2 fragmentTexCoord;

out vec4 color;

uniform float iterations;
uniform float checkDistance;

void main() {
    float fractalScale = 4;
    vec2 current = vec2(0, 0);
    int total_iterations = 0;
    vec2 coord = (fragmentTexCoord - 0.5) * fractalScale;
    for(int i = 0; i < int(iterations); i++) {
        current = vec2(current.x * current.x - current.y * current.y, 2 * current.x * current.y) + coord;
        if (length(current) > checkDistance) {
            total_iterations = i;
            break;
        }
    }
    float c = total_iterations / iterations;
    color = vec4(c, c, c, 1.0);
}