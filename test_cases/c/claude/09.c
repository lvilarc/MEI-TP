#include <assert.h>
#include <stdbool.h>
#include <stddef.h>

bool isNumber(char* s);

int main(void) {
    assert(isNumber("0") == true);
    assert(isNumber("e") == false);
    assert(isNumber("-123.456e789") == true);
    assert(isNumber(".") == false);
    assert(isNumber("+6e-1") == true);
    return 0;
}