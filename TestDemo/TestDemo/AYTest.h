//
//  AYTest.h
//  TestDemo
//
//  Created by April Yang on 2020/3/27.
//  Copyright © 2020 April Yang. All rights reserved.
//

#import <Foundation/Foundation.h>

NS_ASSUME_NONNULL_BEGIN

@interface AYTest : NSObject
@property(nonatomic, assign) NSInteger age;
@property(nonatomic, strong) NSString *name;
-(NSInteger)instanceOne:(BOOL)one;
-(NSInteger)instanceTwo:(BOOL)one;
+(NSInteger)classOne:(BOOL)one;
+(NSInteger)classTwo:(BOOL)one;
@end

NS_ASSUME_NONNULL_END
