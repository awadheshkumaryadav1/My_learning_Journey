
// abstract class Vechicle{
//     abstract void start();

//     void fuel(){
//         System.out.println("fuel is required");
//     }
// }
// class Car extends Vechicle{
//     void start(){
//         System.out.println("car is started");
//     }
// }

// public class abstraction {
//     public static void main(String []args){
//         Car s1=new Car();
//         s1.fuel();
//         s1.start();

//     }
    
// }
abstract class vehicle{
    abstract void start();
    void fuel(){
        System.out.println("fuel is required");
    }

}
class car extends vehicle{
    void start(){
        System.out.println("car is started");

    }
}

public class abstraction{
    public static void main(String []args){
        car S1=new car();
        S1.start();
        S1.fuel();

    }
}
