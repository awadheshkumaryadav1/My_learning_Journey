class animal{
    animal(){
        System.out.println("animal constructor");
    }

}
class dog extends animal{
    dog(){
        System.out.println("dog constructor");
    }
}

public class constructorininheritance {
    public static void main(String[] args) {
        dog d1=new dog();
    }
    
}
