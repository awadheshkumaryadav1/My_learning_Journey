
interface animal{
    void displayA();
}
interface dog {
    void displayB();
}

class cat implements animal,dog{
    public void displayA(){
        System.out.println("class A");
    }
    public void displayB(){
        System.out.println("class Bb");
    }
}

public class multipleinheritance {
    public static void main(String[] args) {
        cat C1=new cat();
        C1.displayA();
        C1.displayB();
        
    }
    
}
