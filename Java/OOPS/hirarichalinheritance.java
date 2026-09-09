class A{
    void displayA(){
        System.out.println("class A");
    }
}
class B extends A{
    void displayB(){
        System.out.println("class B and it is child of class A");
    }
}
class C extends A{
    void displayC(){
        System.out.println("class C and it is child of class A");
    }
}

public class hirarichalinheritance {
    public static void main(String[] args) {
        C C1=new C();
        C1.displayA();
        C1.displayC();

        B B1=new B();
        B1.displayA();  
        B1.displayB();

    
}
}