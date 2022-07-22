class Endpoints:

    def __init__(self):
        return

    def VictimDemographic(self, offense, variable):
        nationalNIBRSVictimDemographicCount = '/api/data/nibrs/' + offense + '/victim/national/' + variable
        return nationalNIBRSVictimDemographicCount

    baseURL = 'https://api.usa.gov/crime/fbi/sapi'