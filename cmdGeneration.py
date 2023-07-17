guide_str = '''
DECTEVCLR01          
DECTEVCLR02          
DECTEVCLR03          
DECTEVCLR04          
DECTEVCLR05          
DECTEVRR26           
DECTEVSLR31          
DECTEVSLR32          
DEVLB1IBR01.vftest.de
DEVLD1IBR01.vftest.de
DEVLF1CLR01          
DEVLF1CLR02          
DEVLF1IBR01.vftest.de
DEVLF1SLR01.vftest.de
DEVLF1SLR02          
DEVLR5SLR01.vftest.de
'''
guide_list = guide_str.split('\n')

template = '''
mvr execute ietf-l3nm-reconcile-vfde inputs {{ device {0} bgp-as 3209 }} commit {{ sync-devices false dry-run-outformat data-extraction-result }}
mvr execute ietf-l3nm-reconcile-vfde inputs {{ device {0} bgp-as 3209 }} commit {{ sync-devices false dry-run-outformat correlated-result }}
mvr execute ietf-l3nm-reconcile-vfde inputs {{ device {0} bgp-as 3209 }} commit {{ sync-devices false dry-run-outformat cli }}
mvr execute ietf-l3nm-reconcile-vfde inputs {{ device {0} bgp-as 3209 }} commit {{ sync-devices false no-networking reconcile {{ keep-non-service-config }} }}
devices device {0} sync-from
l3vpn-ntw vpn-services vpn-service 5 re-deploy reconcile {{ discard-non-service-config }} dry-run
'''
for ge in guide_list:
    if ge:
        print(template.format(ge.strip()), end='\n')
