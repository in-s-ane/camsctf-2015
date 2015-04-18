import java.io.PrintStream;
import java.lang.reflect.Array;

public class givemeflag {
    public givemeflag() {}
    public static void main(String args[]) {
        /*
        if(args.length != 1) {
            System.out.println("You are not worthy of receiving the flag.");
        }
        else {
        */
            int ai1[] = { 4329, 4347, 4301, 4339, 4351, 4301, 4344, 4339, 4324, 4339, 4301, 4351, 4339, 4321, 4326, 4343, 4320, 4335 };
            /*
            int ai[] = new int[args[0].length()];
            for(int i = 0; i < array.getLength(ai1); i++) {
                ai[i] = args[0].charAt(i);
                if((ai[i] ^ 0x1092) != ai1[i] || args[0].length() != array.getLength(ai1)) {
                    system.out.println("You are wrong.");
                    system.exit(0);
                }
            }
            System.out.println((new StringBuilder()).append("Flag: ").append(args[0]).toString());
            */
            String flag = "Flag: ";
            for(int i = 0; i < ai1.length; i++) {
                ai1[i] ^= 0x1092;
                flag += (char) ai1[i];
            }
            System.out.println(flag);
        /*}*/
    }
}
