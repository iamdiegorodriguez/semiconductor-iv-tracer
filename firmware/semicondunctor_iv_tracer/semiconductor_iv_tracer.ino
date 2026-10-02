#include <Wire.h>
#include <Adafruit_MCP4725.h>
#include <Adafruit_INA219.h>

Adafruit_MCP4725 dac;
Adafruit_INA219 ina219;

const int DIODE_PIN = 36;   // VP

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);
  dac.begin(0x60);
  ina219.begin();
  analogReadResolution(12);
}

void loop() {
  for (int step = 0; step <= 4095; step += 16) {
    dac.setVoltage(step, false);
    delay(20);

    float v_sum = 0;
    float i_sum = 0;

    for (int k = 0; k < 5; k++) {
      v_sum += analogReadMilliVolts(DIODE_PIN) / 1000.0;
      i_sum += ina219.getCurrent_mA();
      delay(2);
    }

    float v = v_sum / 5.0;
    float i = i_sum / 5.0;

    Serial.printf("%.4f,%.4f\n", v, i);
  }

  delay(2000);
}