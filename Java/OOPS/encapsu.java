
class Student{
    private String name;
    private int age;
    public void  setdata(String name,int age){
        this.name=name;
        this.age=age;
    }
    public String getName(){
        return name;

    }
    public int getAge(){
        return age;
    }

}

public class encapsu {
    public static void main(String[]args){
        Student s1=new Student();
        s1.setdata("ak",23);
        System.out.println(s1.getName());
        System.out.println(s1.getAge());

    }
}