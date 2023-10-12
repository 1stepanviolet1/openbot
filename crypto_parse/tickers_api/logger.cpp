#include <iostream>


static size_t LOGGER_COUNT = 0;

#define log(msg) std::cout << "LOGGER{" << ++LOGGER_COUNT << "}: "; \
				 std::cout << msg << std::endl;
