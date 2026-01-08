String fingers;

void setup() {
  Serial.begin(115200);

  // 3 = thumb
  // 4 = index finger
  // 5 = middle finger
  // 6 = ring finger
  // 7 = pinky finger
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);

}

void loop() {

  fingers = Serial.readStringUntil('\n');
  fingers.trim();

  if (fingers.charAt(0) == '1') {
    digitalWrite(7, HIGH);
  } else {
    digitalWrite(7, LOW);
  }

  if (fingers.charAt(1) == '1') {
    digitalWrite(6, HIGH);
  } else {
    digitalWrite(6, LOW);
  }

  if (fingers.charAt(2) == '1') {
    digitalWrite(5, HIGH);
  } else {
    digitalWrite(5, LOW);
  }

  if (fingers.charAt(3) == '1') {
    digitalWrite(4, HIGH);
  } else {
    digitalWrite(4, LOW);
  }

  if (fingers.charAt(4) == '1') {
    digitalWrite(3, HIGH);
  } else {
    digitalWrite(3, LOW);
  }
}
