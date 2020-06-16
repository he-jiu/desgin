<template>
	<view>
		<form @submit="formSubmit">
			<view class="content">
				<view>
					<view >
						用户编号：{{_id}}
					</view>
					<view>
						姓名：{{name}}
					</view>
					<view>
						住址：{{address}}
					</view>
				</view>
				
				<view class="page-section page-section-gap">
					<map style="width: 100%; height: 300px;" :latitude="latitude" :longitude="longitude" :markers="marker"></map>
				</view>
				<view class="uni-title uni-common-pl">检查项目</view>
				
				
				<view class="uni-list"> <!-- picker + input -->
					<view class="uni-list-cell"> <!-- picker -->
						<view class="uni-list-cell-left">
							阀门：
						</view>
						<view class="uni-list-cell-db">
							<picker @change="valve"   name='valve' :value="valveindex" :range="array">
								<view class="uni-input">{{array[valveindex]}}</view>
							</picker>
						</view>
					</view>
					
					<view class="uni-list-cell">
						<view class="uni-list-cell-left">
							管道：
						</view>
						<view class="uni-list-cell-db">
							<picker @change="tube" name='tube' :value="tubeindex" :range="array">
								<view class="uni-input">{{array[tubeindex]}}</view>
							</picker>
						</view>
					</view>
					
					<view class="uni-list-cell">
						<view class="uni-list-cell-left">
							设备：
						</view>
						<view class="uni-list-cell-db">
							<picker @change="device" name='device' :value="deviceindex" :range="array">
								<view class="uni-input">{{array[deviceindex]}}</view>
							</picker>
						</view>
					</view>
					
				
					<view class="uni-title uni-common-pl">备注</view><!-- input -->
					
					
					<view class="uni-textarea" >
						<textarea auto-height name='remarks' placeholder="备注"/>
					</view>
					
					<view class="uni-title uni-common-pl">上传照片</view>
					<view>
						<image class='image' @click="onclick" :src='src'></image>
					</view>
				</view>
				
			
				
			</view>
			
			<view class="uni-btn-v">
				<button form-type ="submit" class="submitButton" type="primary">提交</button>	   
			</view>
				
		</form>
		
		
	</view>
</template>

<script>
 var _self;
 var url;
 var imgFiles;
	export default{
		data(){
			return{
				src:'../../static/img/weixin.png',
				valveindex: 0,
				tubeindex: 0,
				deviceindex: 0,
				array: ['请选择','良好', '一般', '需要更换'],
				
				_id:'',
				name:'',
				address:'',
				latitude:0,
			　　longitude: 0,
			　　marker: [
				{
			   　　latitude: 0,//纬度
			   　　longitude: 0,//经度
			   　　rotate:0,   // 旋转度数
			   　　width:20,   //宽
			   　　height:20,   //高
			  　　 alpha:0.5 ,  //透明度
			  　　 
				   callout:{//自定义标记点上方的气泡窗口 点击有效  
				   　　content:'目标位置',//文本
				   　　color:'#ffffff',//文字颜色
				   　　fontSize:14,//文本大小
				   　　borderRadius:2,//边框圆角
				  　　 bgColor:'#00c16f',//背景颜色
				   　　display:'ALWAYS',//常显
				   }
				}]
			}
		},
		
		methods:{
			
			onLoad:function(option){
				// var currentlongitude;
				// var currentlatitude;
				_self=this;
				this._id=JSON.parse(decodeURIComponent(option.item))._id;
				this.name=JSON.parse(decodeURIComponent(option.item)).name;
				this.address=JSON.parse(decodeURIComponent(option.item)).address;
				
				uni.request({
						url:'http://182.92.239.229/getposition',
						data:{
							id:this._id,
						},
						success: (res) => {
							this.marker[0].latitude=parseFloat(res.data[1]);
							this.latitude=parseFloat(res.data[1]);
							this.marker[0].longitude=parseFloat(res.data[0]);
							this.longitude=parseFloat(res.data[0]);
						}
					});
				uni.getLocation({
					success: (res) => {
						console.log(res.latitude)
						console.log(res.longitude)
						
					}
				})
				
			},
			valve: function(e) {

			            this.valveindex = e.target.value

			},
			tube: function(e) {

			            this.tubeindex = e.target.value
			},
			device: function(e) {

			            this.deviceindex = e.target.value
			},
			onclick:function(){//点击图片
				var _self=this;
				
				
			     uni.chooseImage({
			         count: 1,
			         sizeType:['copressed'],
			         success(res) {
			             //因为有一张图片， 输出下标[0]， 直接输出地址
			             imgFiles = res.tempFilePaths[0];
						 _self.src=imgFiles;
			             //console.log(imgFiles);
			             // 上传图片
			             // 做成一个上传对象
			             
			         }
			     })
			 },
			formSubmit:function(e){

				e.detail.value.valve=this.valveindex;
				e.detail.value.tube=this.tubeindex;
				e.detail.value.device=this.deviceindex;
				e.detail.value.userID=this._id;
				e.detail.value.name=this.name;
				e.detail.value.address=this.address;
				
				
				
				if(e.detail.value.valve==0||e.detail.value.tube==0||e.detail.value.device==0||e.detail.value.remarks
				==''){
					uni.showToast({
						icon:'none',
						title:'数据未填写全'
					})
				}
				else{
					uni.uploadFile({//上传文件
					    // 需要上传的地址
					    url:'http://182.92.239.229/upload',
					    // filePath  需要上传的文件
					    filePath: imgFiles,
					    name: 'file',
									
					    success:(res)=>  {
					        // 显示上传信息
							url=res.data ;
							console.log('form发生了submit事件，携带数据为：' + JSON.stringify(e.detail.value))
							e.detail.value.url=url;
							console.log(url);
							
							uni.request({//发出请求
								
								url:'http://182.92.239.229/check',
								data:e.detail.value,
									
							
								success: (res) => {
									console.log(res.data);
									uni.showToast({
										icon:'none',
										title:'添加成功'
									});
									setTimeout(function(){uni.redirectTo({
										url:'../customersList/customersList'
									})},1000)
									
								},
								fail: (res) => {
									uni.showToast({
										icon:'none',
										title:'上传失败'
									})
								}
							});
					    },
						fail: (res) => {
							uni.showToast({
								icon:'none',
								title:'还未选择照片'
							})
						}
					});
					
				}
			}
			
		}
	}
</script>

<style>
	.uni-list-cell{
		display: flex;
		border-top:solid;
		border-color: #C8C7CC;
		border-width: 3rpx;
		
	}
	.uni-list-cell-db{
		margin-left: 50rpx;
	}

	
	.uni-list-cell-left{
		margin-left: 30rpx;
		
	}
	.submitButton{
		width: 100%;
		background: #0FAEFF;

	}
	.uni-textarea{
		border:solid #C8C7CC;
		height: auto;
		
	}
	.add{
		width: 100rpx;
		height: 100rpx;
	}

	.image{
		height: 200rpx;
		width: 200rpx;
	}

</style>
