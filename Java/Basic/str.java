public class str{
    public static void main(String[] args) {
        String str1="ak";
        String str2="ak";
        System.out.println(str1==str2); // true
        System.out.println(str1.equals(str2)); // true
        String str3=new String("ak");
        String str4=new String("ak");
        System.out.println(str3==str4); // false
        System.out.println(str3.equals(str4));

        // string methods
        String str5="Hello World";
        System.out.println(str5.length()); // 11
        System.out.println(str5.toUpperCase()); // HELLO WORLD
        System.out.println(str5.toLowerCase()); // hello world
        System.out.println(str5.charAt(0)); // H
        System.out.println(str5.indexOf("o")); // 4
        System.out.println(str5.substring(0,5)); // Hello 

        

    }
    
}

