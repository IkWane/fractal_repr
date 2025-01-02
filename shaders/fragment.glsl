#version 330 core

in vec2 fragmentTexCoord;

out vec4 color;

uniform float iterations;
uniform float checkDistance;
uniform vec2 constant;
uniform vec2 offset;
uniform float fractalScale;

vec3 hsv2rgb(vec3 c)
{
    vec4 K = vec4(1.0, 2.0 / 3.0, 1.0 / 3.0, 3.0);
    vec3 p = abs(fract(c.xxx + K.xyz) * 6.0 - K.www);
    return c.z * mix(K.xxx, clamp(p - K.xxx, 0.0, 1.0), c.y);
}

void main() {
    int total_iterations = 0;
    vec2 coord = (fragmentTexCoord - 0.5) * fractalScale + offset;
    vec2 current = coord;
    for(int i = 0; i < int(iterations); i++) {
        current = vec2(current.x * current.x - current.y * current.y, 2 * current.x * current.y) + constant;
        if (length(current) > checkDistance) {
            total_iterations = i;
            break;
        }
    }
    float intensity = total_iterations / iterations;
    vec3 c = vec3(0.0);
    if (intensity != 0) {
        c = hsv2rgb(vec3(1.0-intensity, 1.0, 1.0));
    }
    color = vec4(c, 1.0);
}