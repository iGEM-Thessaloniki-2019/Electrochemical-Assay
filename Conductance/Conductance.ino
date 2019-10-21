int cnt=0;
void setup() {
  analogWriteResolution(12);
  Serial.begin(115200);
}

void loop() {
  cnt++;
  Serial.print("Measurement No: ");
  Serial.println(cnt);
  for (int i = 0; i < 2000; i=i+10) {
    analogWrite(DAC0, i);
    Serial.print(float(analogRead(A2)+10)/310);
    Serial.print(',');
    Serial.println(float(analogRead(A1))/310);
    delay (100);
  }
  delay (30000);
}
