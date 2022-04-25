package termProject;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class Substring implements Runnable {
	String base;
	AtomicInteger index;
	
	public Substring(String s) {
		base = s;
		index = new AtomicInteger(-1);
	}
	
	public int findIndex(String search) {
		int last_index = this.base.length() - search.length() + 1;
		for(int i = 0; i < last_index; i++) {
			int end = i + search.length();
			if(search.equals(base.substring(i, end))) {
				return i;
			}
		}
		return -1;
	}
	
}

public static void
	
	public int findIndex_parallel(String search) {
		int last_index = this.base.length() - search.length() + 1;
		List<Thread> list = new ArrayList<>();
		for(int i = 0; i < last_index; i++) {
			Thread t = new Thread(this);
			t.start();
			list.add(t);
		}
		for(Thread t : list) {
            try {
                t.join();
            }
            catch(Exception e) {
                e.printStackTrace();
            }
        }
		return -1;
	}
	
	@Override
	public void run() {
		
	}
}
