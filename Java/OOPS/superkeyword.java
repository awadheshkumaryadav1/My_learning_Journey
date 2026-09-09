class a{
    void show(){
        System.out.println("hii");
    }
}
class b extends a{
    void show(){
        super.show();
        System.out.println("hello");
    }
}

public class superkeyword {
    public static void main(String[] args) {
        b B1=new b();
        B1.show();
    }
    
}
