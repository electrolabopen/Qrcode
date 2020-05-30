
char lectura;
void setup(){
 pinMode (13, OUTPUT); //pin configurado como salida
 Serial.begin(9600);
}
 
void loop(){
 
  if(Serial.available() >= 1){ // disponibilidad para recibir los datos de python
  lectura = Serial.read();

  if(lectura == 'h'){
    digitalWrite(13,HIGH);
  }
  else{
    digitalWrite(13,LOW);
  }


   
 }

}
