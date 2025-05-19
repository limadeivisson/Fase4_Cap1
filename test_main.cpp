#include <Arduino.h>
#include <unity.h>

void test_exemplo() {
  TEST_ASSERT_EQUAL(1, 1);
}

void setup() {
  UNITY_BEGIN();
  RUN_TEST(test_exemplo);
  UNITY_END();
}

void loop() {}
