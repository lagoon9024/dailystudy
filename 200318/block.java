import java.security.*;
import java.util.ArrayList;


public class block {
	private static ArrayList<Node> Blockchain = new ArrayList<Node>();
	private static void mining(String data) {
		if(Blockchain.isEmpty()) Blockchain.add(new Node(data));
		else {
			String prevHash = Blockchain.get(Blockchain.size()-1).gethash();
			Blockchain.add(new Node(data,prevHash));
		}
	}
	
	public static void main(String[] args){
		mining("GENESIS BLOCK");
		mining("2nd");
		mining("3rd");
		for(int i=0; i<Blockchain.size();++i) {
			Blockchain.get(i).printBlock();
		}
	}
}

class Node {
	private String hash;
	private String prevhash;
	private String data;
	private int nonce=0;
	
	public Node(String data) {
		this.data = data;
		newBlock();
	}
	
	public Node(String data, String prevhash) {
		this.data= data;
		this.prevhash = prevhash;
		newBlock();
	}
	
	public void printBlock() {
		System.out.println("NONCE :: "+nonce);
		System.out.println("DATA :: "+data);
		System.out.println("PREVIOUS HASH :: "+prevhash);
		System.out.println("HASH :: "+hash +"\n");
	}
	
	public String gethash() {
		return this.hash;
	}
	
	private void newBlock() {
		if(prevhash!=null) {
			while(hash == null || !(hash.substring(0,5).equals("00000"))) {
				++nonce;
				hash = sha256(prevhash+data+Integer.toString(nonce));
			}
		}
		else
			hash=sha256(data+Integer.toString(nonce));
	}
	
	public static String sha256(String msg){
		String SHA;
		try {
		MessageDigest md = MessageDigest.getInstance("SHA-256");
		md.update(msg.getBytes());
		SHA = bytesToHex1(md.digest());
		}catch(NoSuchAlgorithmException e) {
			SHA = null;
		}
		return SHA;
	}
	
	public static String bytesToHex1(byte[] bytes) {
		StringBuilder builder = new StringBuilder();
		for(byte b: bytes) {
			builder.append(String.format("%02x",b));
		}
		return builder.toString();
	}	
}