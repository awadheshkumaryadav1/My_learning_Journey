class ABCD{
    void show(){
        System.out.println("display");
    }
}
class A extends ABCD {
    @Override
    void show(){
        System.out.println("print output");
    }
}
public class runtimepolyoveride {
    public static void main(String[] args) {
        ABCD obj=new A();
        obj.show();
    
}
}
