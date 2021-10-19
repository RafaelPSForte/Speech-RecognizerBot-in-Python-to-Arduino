int  LED = 2;
char leitura;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
}

void loop() {

  if (Serial.available() > 0){
    leitura = Serial.read();
    Serial.println(leitura);
    if (leitura == 'l'){
      digitalWrite(LED,HIGH);
      delay(1000);
      }
    if (leitura == 'd'){
      digitalWrite(LED,LOW);
      delay(1000);
    }
   }
  }
