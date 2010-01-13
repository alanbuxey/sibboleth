package au.org.arcs.auth.shibboleth;

import java.util.Iterator;
import java.util.Map;
import java.util.TreeSet;

import org.python.core.PyInstance;
import org.python.core.PyObject;

import au.org.arcs.jcommons.utils.ArcsSecurityProvider;


public class DummyIdpObject extends IdpObject {
	
	private String sel = "Dummy";

	@Override
	public String get_idp() {
		return sel;
	}
	
	@Override
	public PyInstance prompt(ShibbolethClient shibboleth) {
		return null;
	}
	
	public static void main(String[] args) throws InterruptedException {

		java.security.Security.addProvider(new ArcsSecurityProvider());

		java.security.Security.setProperty("ssl.TrustManagerFactory.algorithm",
				"TrustAllCertificates");

//		IdpObject idp = new IdpObject() {
//			
//			@Override
//			public void set_idps(Map<String, String> idps) {
//				
//				this.idpList = new TreeSet<String>(idps.keySet());
//				
//				for ( String idp : idpList ) {
//					System.out.println(idp);
//				}
//				
//			}
//			
//			@Override
//			public PyInstance prompt(ShibbolethClient shibboleth) {
//				// TODO Auto-generated method stub
//				return null;
//			}
//			
//			@Override
//			public String get_idp() {
//				// TODO Auto-generated method stub
//				return null;
//			}
//		};
		
		IdpObject idpO = new DummyIdpObject();
		
		CredentialManager cm = new DummyCredentialManager();
		
		Shibboleth shib = new Shibboleth(idpO, cm);

		String url = "https://slcs1.arcs.org.au/SLCS/login";
		shib.openurl(url);
		
		for (String idp : idpO.getIdps() ) {
			System.out.println(idp);
		}

		System.out.println("Finished.");


	}

}
