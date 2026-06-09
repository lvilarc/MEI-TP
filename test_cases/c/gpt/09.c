#include <assert.h>
#include <stdbool.h>

bool isNumber(char *s);

int main(void) {
    assert(isNumber("0") == true);
    assert(isNumber("-.9") == true);
    assert(isNumber("+6e-1") == true);
    assert(isNumber(".") == false);
    assert(isNumber("95a54e53") == false);

    return 0;
}