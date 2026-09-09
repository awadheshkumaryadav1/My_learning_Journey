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
class C extends B{
    void displayC(){
        System.out.println("class C and it is child of class B");
    }
}

public class multilevelinheritence {
    public static void main(String[] args) {
        C C1=new C();
        C1.displayB();
        C1.displayC();

        C1.displayA(); 
}
}
