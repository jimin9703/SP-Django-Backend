from rest_framework import viewsets, status
from rest_framework.response import Response
from travel.entity.models import Travel
from travel.serializer import TravelSerializer
from travel.service.travel_service_impl import TravelServiceImpl


class TravelView(viewsets.ViewSet):
    queryset = Travel.objects.all()

    travelService = TravelServiceImpl.getInstance()

    def list(self, request):
        travelList = self.travelService.list()
        serializer = TravelSerializer(travelList, many=True)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            # productImage = request.FILES.get('productImage')
            travelName = data.get('travelName')
            travelLocation = data.get('traveLocation')
            travelProperty = data.get('travelProperty')
            travelContent = data.get('travelContent')
            travelPrice = data.get('travelPrice')


            if not all([productImage, productName, productPrice, productDescription]):
                return Response({ 'error': '모든 내용을 채워주세요!' },
                                status=status.HTTP_400_BAD_REQUEST)

            self.productService.createProduct(productName, productPrice,
                                              productDescription, productImage)

            serializer = ProductSerializer(data=request.data)
            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('상품 등록 과정 중 문제 발생:', e)
            return Response({ 'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)