//most of the code has been taken from "http://active-ist.sourceforge.net/jaus++/examples/tutorial_02_a.html" and modified as per the solution
//after trying to understand the code as much as possible
#include <jaus/core/component.h>
#include <cxutils/keyboard.h>
#include <iostream>

int main(int argc, char* argv[])
{
     JAUS::Component component;
     JAUS::Discovery* discoveryService = NULL;
     discoveryService = component.DiscoveryService();
     discoveryService->SetSubsystemIdentification(JAUS::Subsystem::Vehicle,
                                                 "Robot");
     discoveryService->SetNodeIdentification("Primary Computer");
     discoveryService->SetComponentIdentification("Baseline");
 
     JAUS::Address componentID(1000, 1, 2);

     std::cout << "Initializing component...";
     if(component.Initialize(componentID) == false)
     {
         std::cout << "Failed to initialize component [" << componentID.ToString() << "]\n";
         return 0;
     }
     std::cout << "Success!\n";

     JAUS::Time::Stamp displayStatusTimeMs = JAUS::Time::GetUtcTimeMs();
     while(true)
     {
         JAUS::Management* managementService = NULL;
         managementService = component.ManagementService();
         if(managementService->GetStatus() == JAUS::Management::Status::Shutdown)
         {
             break;
         }
 
         if(JAUS::Time::GetUtcTimeMs() - displayStatusTimeMs > 500)
         {

             JAUS::Subsystem::Map discoveredSubsystems;
             discoveryService->GetSubsystems(discoveredSubsystems);
             std::cout << "======================================================\n";
 
             JAUS::Subsystem::Map::iterator subsystem;
             for(subsystem = discoveredSubsystems.begin();
                 subsystem != discoveredSubsystems.end();
                 subsystem++)
             {
                 std::cout << "Subsystem: "
                           << subsystem->first
                           << " Identification: "
                           << subsystem->second->mIdentification
                           << std::endl;
                 //this segment is to send query for 'QueryIdentification'
                 JAUS::Address::List componentsWithQuery;
                 componentsWithQuery = subsystem->second->GetComponentsID();
                 JAUS::Address::List::iterator t;
                 for(t = componentsWithQuery.begin();
                     t != componentsWithQuery.end();
                     t++)
                 {
                     if( (*t) != component.GetComponentID())
                     {
                         JAUS::QueryIdentification query;
                         query.SetDestinationID( (*t) );
                         query.SetSourceID(component.GetComponentID());
                         JAUS::ReportIdentification response;
                         std::cout << "\tSending Query to " << t->ToString() << std::endl;
                         if(component.Send(&query, &response, 1000))
                         {
                             std::cout << "\tReceived Response Message!\n\t";
                             response.Print();
                         }
                     }
                 }
                 //this segment is to send query for 'QueryHeartBeatPulse'
                 JAUS::Address::List componentsWithLiveness;
                 componentsWithLiveness = subsystem->second->GetComponentsWithService(JAUS::Liveness::Name);
                 JAUS::Address::List::iterator c;
                 for(c = componentsWithLiveness.begin();
                     c != componentsWithLiveness.end();
                     c++)
                 {
                     if( (*c) != component.GetComponentID())
                     {
                         JAUS::QueryHeartbeatPulse query;
                         query.SetDestinationID( (*c) );
                         query.SetSourceID(component.GetComponentID());
                         JAUS::ReportHeartbeatPulse response;
                         std::cout << "\tSending Query to " << c->ToString() << std::endl;
                         if(component.Send(&query, &response, 1000))
                         {
                             std::cout << "\tReceived Response Message!\n\t";
                             response.Print();
                         }
                     }
                 }
                 //this segment is to send query for 'QueryTransportPolicy'
                 JAUS::Address::List componentsWithTransport;
                 componentsWithTransport = subsystem->second->GetComponentsWithService(JAUS::Transport::Name);
                 JAUS::Address::List::iterator d;
                 for(d = componentsWithTransport.begin();
                     d != componentsWithTransport.end();
                     d++)
                 {
                     if( (*d) != component.GetComponentID())
                     {
                         JAUS::QueryTransportPolicy query;
                         query.SetDestinationID( (*d) );
                         query.SetSourceID(component.GetComponentID());
                         JAUS::ReportTransportPolicy response;
                         std::cout << "\tSending Query to " << d->ToString() << std::endl;
                         if(component.Send(&query, &response, 1000))
                         {
                             std::cout << "\tReceived Response Message!\n\t";
                             response.Print();
                         }
                     }
                 }
             } 

             JAUS::Subsystem::DeleteSubsystemMap(discoveredSubsystems);
             displayStatusTimeMs = JAUS::Time::GetUtcTimeMs();
        }
 
         if(CxUtils::GetChar() == 27)
        {
            break;
        }
 
        CxUtils::SleepMs(1);
    }
    component.Shutdown();
    return 0;
}

  183 

  184 

  185 

  186 /* End of File */

  187 