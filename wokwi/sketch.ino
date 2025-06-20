#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// LCD I2C: endereço 0x27, 16 colunas x 2 linhas
LiquidCrystal_I2C lcd(0x27, 16, 2);

// Variáveis simuladas e otimizadas
int umidade = 0;
int nutrientes = 0;
char status_irrigacao[16];

void setup() {
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();

  lcd.setCursor(0, 0);
  lcd.print("Iniciando...");
  delay(1000);
}

void loop() {
  // Simula valores de sensores
  umidade = random(20, 90);
  nutrientes = random(50, 90);

  // Regra simples para irrigação
  if (umidade < 40 && nutrientes > 60) {
    strcpy(status_irrigacao, "IRRIGANDO");
  } else {
    strcpy(status_irrigacao, "OK");
  }

  // Atualiza LCD
  lcd.clear();
  lcd.setCursor(0, 0);
  lcd.print("U:");
  lcd.print(umidade);
  lcd.print("% N:");
  lcd.print(nutrientes);

  lcd.setCursor(0, 1);
  lcd.print("Status:");
  lcd.print(status_irrigacao);

  // Envia dados para o Serial Plotter
  Serial.print("Umidade:");
  Serial.print(umidade);
  Serial.print(" Nutrientes:");
  Serial.println(nutrientes);

  delay(2000); // Atualiza a cada 2 segundos
}
