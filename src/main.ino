#include <DHT.h>

#define DHTPIN 15
#define DHTTYPE DHT22
DHT dht(DHTPIN, DHTTYPE);

#define LDR_PIN 34
#define P_SENSOR_PIN 18
#define K_SENSOR_PIN 19
#define RELAY_PIN 5

void setup() {
  Serial.begin(115200);
  dht.begin();

  pinMode(P_SENSOR_PIN, INPUT_PULLUP);
  pinMode(K_SENSOR_PIN, INPUT_PULLUP);
  pinMode(RELAY_PIN, OUTPUT);
}

void loop() {
  float humidity = dht.readHumidity();
  int ldrValue = analogRead(LDR_PIN);
  bool fosforo = digitalRead(P_SENSOR_PIN) == LOW;
  bool potassio = digitalRead(K_SENSOR_PIN) == LOW;

  bool irrigar = humidity < 50 || !fosforo || !potassio || ldrValue < 500;
  digitalWrite(RELAY_PIN, irrigar ? HIGH : LOW);

  Serial.print("Umidade: "); Serial.print(humidity);
  Serial.print(" | pH (sim): "); Serial.print(ldrValue);
  Serial.print(" | Fósforo: "); Serial.print(fosforo ? "Sim" : "Não");
  Serial.print(" | Potássio: "); Serial.print(potassio ? "Sim" : "Não");
  Serial.print(" | Bomba: "); Serial.println(irrigar ? "Ligada" : "Desligada");

  delay(3000);
}
