<template>
	<view class='content'>
		<view class="scv">
			<map style="width: 100%; height: 300px;" scale="16" :latitude="latitude" :longitude="longitude" :markers="marker" @callouttap='callouttap' ></map>
			<view class="userMessage" v-for="(user,index) in users" :key='index' @tap="userCheck(index)"  >
				<view v-bind:class="{scv2:user.emergency}">姓名：{{user.name}},	住址：{{user.address}}</view>
			</view>
		</view>
	</view>
	
</template>

<script>
	var _self;
	export default{
		data(){
			return{
				users:[],
				latitude: 40.013307,//纬度
				longitude: 118.685715,//经度
				marker:[],
				array:[]
			}
		},
		methods:{
			onLoad:function(){
				uni.request({
					url:'http://182.92.239.229/getchecklist',
					success: (res) => {
						this.users=res.data;
						console.log(this.users)
						// let defaultmarker = this.defaultmarker;
						let users=this.users;
						_self=this;
						for(var i=0;i<users.length;i++){
							let defaultmarker={
								id:0,
								latitude: 0,//纬度
								longitude: 0,//经度
								width:20,   //宽
								height:20,   //高
								iconPath:'',
								callout:{//自定义标记点上方的气泡窗口 点击有效  
								　　content:'',//文本
								　　color:'#ffffff',//文字颜色
								　　fontSize:14,//文本大小
									borderRadius:2,//边框圆角
									bgColor:'#00c16f',//背景颜色
									display:'BYCLICK',
								}
							};
							defaultmarker['id']=parseInt(users[i]['_id']);
							defaultmarker['latitude']=users[i]['latitude'];
							defaultmarker['longitude']=users[i]['longitude'];
							defaultmarker['callout']['content']=users[i]['address'];
							if (users[i]['emergency']==false){
								defaultmarker['iconPath']='../../static/img/emergencylocation.png';
							}
							_self.array.push(defaultmarker);
						}
						_self.marker=_self.array;
						
					}
				})
			},
			
			callouttap:function(e){
				console.log(e.detail)
				for(var i=0;i<this.users.length;i++){
					if(this.users[i]['_id']==e.detail['markerId']){
						uni.redirectTo({
							url:'../check/check?item='+encodeURIComponent(JSON.stringify(this.users[i]))
						})
					}
				}
				
			},
				
			userCheck:function(index){
				
				uni.redirectTo({
					url:'../check/check?item='+encodeURIComponent(JSON.stringify(this.users[index]))
				})
			}
			
		}

	}
	
</script>

<style>
	.scv{
		background: #F8F8F8;
	}
	.userMessage{
		height: 100rpx;
		border-bottom:solid;
		border-bottom-color: #C8C7CC;
		border-bottom-width: 3rpx;
		margin-left: 10rpx;
		margin-right: 10rpx;
		display: flex;
	}
	
	.userText{
		margin-left: 20rpx;
		margin-top: 20rpx;
	}
	.userImage{
		width: 70rpx;
		height: 70rpx;
		margin-left: 10rpx;
		margin-top: 15rpx;
	}
	 .scv2{
		background: #f80004;
		height: 100rpx;
		border-bottom:solid;
		border-bottom-color: #C8C7CC;
		border-bottom-width: 3rpx;
	 }

</style>
